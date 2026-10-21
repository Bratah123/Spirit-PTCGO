from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import gust_then, recover_from_discard


async def _alluring_dance_confuse(ctx, new_active):
    await ctx.apply_special_condition(new_active, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="016c5ef3-65fa-5a96-ad24-48f948a78e74",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Entangling Control",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon. The new Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_then(_alluring_dance_confuse),
        ),
        Attack(
            title="Trash Tentacle",
            game_text="Put a card from your discard pile into your hand.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=recover_from_discard(count=1, minimum=1, reveal=False, to='hand'),
        ),
    ],
)