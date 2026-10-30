"""STUB: effect not implemented — do not guess mechanics.
Manectric ex (EX8 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import disconnect_lock_items, mega_shot_discard_lightning_snipe


card = PokemonCardDef(
    guid="d18f0029-62c0-5e04-bbed-bb23f630d31c",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectricex.Name",
    display_name="Manectric ex",
    searchable_by=["Manectric ex", "Stage 1", "ex", "Manectricex"],
    subtypes=["Stage 1", "ex"],
    collector_number=101,
    set_code="EX8",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Disconnect",
            game_text="Your opponent can't play any Trainer cards (except for Supporter cards) from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=disconnect_lock_items(),
        ),
        Attack(
            title="Mega Shot",
            game_text="Discard all Lightning Energy attached to Manectric ex and then choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=mega_shot_discard_lightning_snipe(),
        ),
    ],
)