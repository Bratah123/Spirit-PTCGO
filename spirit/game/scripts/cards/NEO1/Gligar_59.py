from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1e53985b-f8a8-5520-af8b-c08e712078da",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=207,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
