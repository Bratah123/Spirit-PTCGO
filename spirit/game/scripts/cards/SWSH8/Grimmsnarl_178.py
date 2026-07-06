from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b7c3f347-56bc-582d-b9ca-36de009c0bc0",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2", "Single Strike", "Grimmsnarl"],
    subtypes=["Stage 2", "Single Strike"],
    collector_number=178,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
        ),
        Attack(
            title="Rear Attack",
            game_text="If you have 2 or fewer Benched Pok\u00e9mon, this attack does 140 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)