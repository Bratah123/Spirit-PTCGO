"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Electrike (EX4 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import flip_attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


card = PokemonCardDef(
    guid="2f2c8867-3afb-536c-9d8a-adb8d6949c9b",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasElectrike.Name",
    display_name="Team Aqua's Electrike",
    searchable_by=["Team Aqua's Electrike", "Basic", "TeamAquasElectrike"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=309,
    abilities=[
        Attack(
            title="Random Spark",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(10, pool='any'),
        ),
        Attack(
            title="Plasma",
            game_text="Flip a coin. If heads, search your discard pile for a Lightning Energy card and attach it to Team Aqua's Electrike.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            # STUB: attack effect not implemented
            effect=flip_attach_from_discard(predicate=lambda c: is_basic_energy_card(c) and energy_provides_type(c, PokemonTypes.LIGHTNING.value)),
        ),
    ],
)