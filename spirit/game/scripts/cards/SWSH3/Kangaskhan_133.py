from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="055d029d-7631-5b1c-8829-ce111fec5a63",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name",
    display_name="Kangaskhan",
    searchable_by=["Kangaskhan", "Basic", "Kangaskhan"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Rally Back",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack from your opponent's Pok\u00e9mon during their last turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)