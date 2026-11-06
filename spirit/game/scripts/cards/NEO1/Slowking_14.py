from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import mind_games_passive


card = PokemonCardDef(
    guid="915a74ad-3fb3-5c0e-8347-cf12cca18bc6",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Mind Games",
            game_text="Whenever your opponent plays a Trainer card, you may flip a coin. If heads, that card does nothing. Put it on top of your opponent's deck. This power can't be used if Slowking is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=mind_games_passive,
        ),
        Attack(
            title="Mind Blast",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage and the Defending Pok\u00e9mon is now Confused. If tails, this attack does 20 damage.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=20,
            damage_operator="+",
            effect=condition_attack(
                SpecialConditions.CONFUSED, flip=True, heads_bonus_damage=10),
        ),
    ],
)
