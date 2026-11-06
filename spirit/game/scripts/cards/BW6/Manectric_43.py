from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, damage_per, count_energy


card = PokemonCardDef(
    guid="5f31340c-ace0-53c5-8ac5-f6fdfda4da04",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Energy Crush",
            game_text="Does 20 damage times the amount of Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_energy('opponent'), 20),
        ),
        Attack(
            title="Flash Impact",
            game_text="Does 20 damage to 1 of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=snipe_attack(20, pool='any', side='mine', also_base=True, apply_modifiers=False, prompt='Choose 1 of your Pokémon to take 20 damage'),
        ),
    ],
)