from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="fb0e10bb-2717-539c-a3c9-ed736aa611c3",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=203,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Girafarig.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Psybeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
