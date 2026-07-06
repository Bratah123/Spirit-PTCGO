from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a0033ec6-9849-56b2-9fb9-c772b820d070",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2", "Grimmsnarl"],
    subtypes=["Stage 2"],
    collector_number=125,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Ability(
            title="Dark Oath",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon's attacks cost Colorless more.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)