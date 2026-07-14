from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on

card = PokemonCardDef(
    guid="925a7ce1-8534-503b-a370-8c12ab0674bc",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Single Strike", "Morpeko"],
    subtypes=["Basic", "Single Strike"],
    collector_number=179,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Explosive Discontent",
            game_text="This attack does 30 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 30),
        ),
    ],
)