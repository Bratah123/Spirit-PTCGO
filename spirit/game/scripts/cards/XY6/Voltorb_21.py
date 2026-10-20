from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, recoil_attack


card = PokemonCardDef(
    guid="3225b76a-b488-53f1-97c4-f475770e8e69",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic", "Voltorb"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="XY6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=100,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Big Explosion",
            game_text="This Pok\u00e9mon does 60 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=recoil_attack(60),
        ),
    ],
)