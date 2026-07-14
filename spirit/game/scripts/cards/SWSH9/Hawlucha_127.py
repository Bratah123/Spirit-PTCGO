from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import is_evolution_pokemon


def _defender_is_evolution(ctx):
    defender = ctx.opponent_active()
    return defender is not None and is_evolution_pokemon(defender)


card = PokemonCardDef(
    guid="f37e9d8d-47bb-57b9-bb7c-3a836a6bb2d8",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=701,
    abilities=[
        Attack(
            title="Showboating Pose",
            game_text="Attach up to 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=2, minimum=0,
                target=lambda p: not is_in_active_spot(p),
                prompt="Choose up to 2 basic Energy cards to attach to a Benched Pok\u00e9mon",
            ),
        ),
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_defender_is_evolution, 30),
        ),
    ],
)