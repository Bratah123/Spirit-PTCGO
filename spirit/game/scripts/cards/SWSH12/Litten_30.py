from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c353cae3-db6b-5ab8-8c66-8cd820ca3260",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    display_name="Litten",
    searchable_by=["Litten", "Basic", "Litten"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=725,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Reprisal",
            game_text="This attack does 20 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 20),
        ),
    ],
)