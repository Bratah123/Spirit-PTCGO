from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import extra_energy_damage
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="4f8db4b7-f36f-536a-850d-6b191a26364c",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra",
    searchable_by=["Seadra", "Stage 1", "Seadra"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Energy Cannon",
            game_text="Does 20 damage plus 10 more damage for each Energy attached to Seadra but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=extra_energy_damage(10, base=20),
        ),
        Attack(
            title="Water Arrow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=snipe_attack(30, pool="any"),
        ),
    ],
)