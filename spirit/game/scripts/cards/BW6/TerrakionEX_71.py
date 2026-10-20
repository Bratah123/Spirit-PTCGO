from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a60b9bd-115a-506b-82c2-11cfedc54886",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TerrakionEX.Name",
    display_name="Terrakion-EX",
    searchable_by=["Terrakion-EX", "Basic", "EX", "TerrakionEX"],
    subtypes=["Basic", "EX"],
    collector_number=71,
    set_code="BW6",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Pump-up Smash",
            game_text="Attach 2 basic Energy cards from your hand to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)