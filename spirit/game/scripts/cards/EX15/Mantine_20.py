"""STUB: effect not implemented — do not guess mechanics.
Mantine δ (EX15 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import power_circulation, spiral_drain_heal
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="814e0f07-3c59-5461-aba1-ecdace6bdbc9",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine δ",
    searchable_by=["Mantine \u03b4", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=226,
    abilities=[
        Ability(
            title="Power Circulation",
            game_text="Once during your turn (before your attack), you may search your discard pile for a basic Energy card, show it to your opponent, and put it on top of your deck. If you do, put 1 damage counter on Mantine. This power can't be used if Mantine is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=power_circulation(),
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 1 damage counter from Mantine.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=spiral_drain_heal(1),
        ),
    ],
)