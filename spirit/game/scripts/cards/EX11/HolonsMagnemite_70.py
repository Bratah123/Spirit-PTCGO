"""EX11 Delta Species — Holon dual-mode Energy attach.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="9e40c3d6-4683-5566-bb96-fca45d20ecd9",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsMagnemite.Name",
    display_name="Holon's Magnemite",
    searchable_by=["Holon's Magnemite", "Basic", "HolonsMagnemite"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=81,
    attachable_as_energy=True,
    energy_provides=[[PokemonTypes.COLORLESS]],
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(10, pool='any'),
        ),
    ],
)