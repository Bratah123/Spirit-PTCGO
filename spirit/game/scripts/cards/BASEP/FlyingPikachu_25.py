from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="d82a5558-02ee-5888-a721-9a762571bed5",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachu.Name",
    display_name="Flying Pikachu",
    searchable_by=["Flying Pikachu", "Basic", "FlyingPikachu"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Flying Pikachu; if tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=flip_or_nothing(then=protect_next_turn(prevent=True, effects_too=True)),
        ),
    ],
)
