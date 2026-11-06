from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ef8f79f8-3568-540e-a518-60ed713e74cd",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    display_name="Gulpin",
    searchable_by=["Gulpin", "Basic", "Gulpin"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=316,
    abilities=[
        Attack(
            title="Poison Gas",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)