from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f959df23-74b4-575f-a3c4-ad53b717a10d",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name",
    display_name="Incineroar",
    searchable_by=["Incineroar", "Stage 2", "Incineroar"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Secret Attack",
            game_text="Choose an attack from 1 of this Pok\u00e9mon's previous Evolutions and use it as this attack.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flare Shot",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=180,
            effect=unimplemented,
        ),
    ],
)