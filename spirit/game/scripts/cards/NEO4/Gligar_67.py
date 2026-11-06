from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="f97a3287-805b-5d76-84bc-c7ed692411a4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=207,
    abilities=[
        Attack(
            title="Stun Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED, flip=True),
        ),
    ],
)
