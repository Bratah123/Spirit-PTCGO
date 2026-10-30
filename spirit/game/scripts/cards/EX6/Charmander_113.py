from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on

card = PokemonCardDef(
    guid="2be0783b-f31a-50e5-95f3-0aa03eb049b3",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="EX6",
    rarity=Rarities.RareSecret,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Charmander.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=10),
        ),
    ],
)