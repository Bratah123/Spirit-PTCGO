from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="3b51afab-da44-58d4-935d-a30e014ed572",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name",
    display_name="Emolga",
    searchable_by=["Emolga", "Basic", "Emolga"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="CZ",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=587,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)