from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a6a09ff7-316b-5f87-9210-161d286fb919",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Druddigon"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=621,
    abilities=[
        Attack(
            title="Revenge",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack from your opponent's Pok\u00e9mon during their last turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)