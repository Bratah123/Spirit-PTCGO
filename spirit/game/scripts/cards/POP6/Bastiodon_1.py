from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import sand_veil_bench_protect, anger_revenge_snipe


card = PokemonCardDef(
    guid="97355b86-2b6b-53ab-b2f1-46626e02761c",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="POP6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=411,
    abilities=[
        Ability(
            title="Protective Wall",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=sand_veil_bench_protect(),
            effect=None,
        ),
        Attack(
            title="Anger Revenge",
            game_text="If Bastiodon was damaged by an attack during your opponent's last turn, this attack does 40 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=anger_revenge_snipe(40),
        ),
    ],
)
