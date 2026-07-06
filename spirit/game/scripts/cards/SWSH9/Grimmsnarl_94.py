from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1d3a5b87-4fe8-5598-a361-0a998602c6b9",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2", "Grimmsnarl"],
    subtypes=["Stage 2"],
    collector_number=94,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Longhair Shot",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each Darkness Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)