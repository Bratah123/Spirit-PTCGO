from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import (
    apply_defender_attack_cost_raise, apply_defender_retreat_cost_raise,
)


async def _shaky_wave(ctx):
    await ctx.deal_damage()
    await apply_defender_attack_cost_raise(ctx)
    await apply_defender_retreat_cost_raise(ctx)

card = PokemonCardDef(
    guid="e8724276-bcbe-5609-b55d-5dbd5e83bda4",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=90,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Shaky Wave",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=_shaky_wave,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)