from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0cd42222-0589-5774-96c9-8e9d4221593b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StarmieV.Name",
    display_name="Starmie V",
    searchable_by=["Starmie V", "Basic", "V", "StarmieV"],
    subtypes=["Basic", "V"],
    collector_number=166,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=121,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Energy Spiral",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)