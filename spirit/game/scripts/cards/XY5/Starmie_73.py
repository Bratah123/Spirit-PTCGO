from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_energy


def _same_energy(ctx):
    return ctx.defender is not None and count_energy('self')(ctx) == count_energy('defender')(ctx)


card = PokemonCardDef(
    guid="c3a6c661-2a50-5994-9a68-05c6a5814732",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Synchro Star",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached to them, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_same_energy, 60),
        ),
    ],
)