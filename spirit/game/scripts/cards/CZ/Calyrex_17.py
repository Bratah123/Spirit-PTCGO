from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9656d298-ea31-505e-adbd-b6bb0bc42a6c",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Calyrex.Name",
    display_name="Calyrex",
    searchable_by=["Calyrex", "Basic", "Calyrex"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=898,
    abilities=[
        Attack(
            title="King's Instructions",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Bloomshine",
            game_text="Heal 20 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)