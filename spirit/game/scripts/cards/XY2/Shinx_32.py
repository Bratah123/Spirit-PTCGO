from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="7ee1e958-13c2-53d5-84a4-ac3f78bc2203",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Shinx"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=403,
    abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
        ),
    ],
)