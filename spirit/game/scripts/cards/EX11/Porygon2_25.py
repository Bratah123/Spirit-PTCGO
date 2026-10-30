"""STUB: effect not implemented — do not guess mechanics.
Porygon2 (EX11 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.card_effects.ex import backup_draw_to, backup_draw_to_condition, machine_burst_if_tm
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="3e7e0e66-6784-587c-a322-e5fd88a6fdbc",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1", "Porygon2"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Backup",
            game_text="Once during your turn (before your attack), if you have less than 6 cards in your hand, you may draw cards until you have 6 cards in your hand. This power can't be used if Porygon2 is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=backup_draw_to_condition(6),
            effect=backup_draw_to(6),
        ),
        Attack(
            title="Machine Burst",
            game_text="If Porygon2 has a Technical Machine card attached to it, the Defending Pok\u00e9mon is now Asleep and Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=machine_burst_if_tm(),
        ),
    ],
)