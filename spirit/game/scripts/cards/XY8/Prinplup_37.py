from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="0cca3079-2043-5d2b-8c4f-d84ee1201ed1",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    display_name="Prinplup",
    searchable_by=["Prinplup", "Stage 1", "Prinplup"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)