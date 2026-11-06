from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import tailwind, tailwind_condition


card = PokemonCardDef(
    guid="14edd5ff-b262-59d1-ad22-004f2f58eba5",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Tailwind",
            game_text="Once during your turn (before your attack), if Dragonite is on your Bench, you may reduce your Active Pok\u00e9mon's Retreat Cost to 0.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=tailwind_condition,
            effect=tailwind,
        ),
        Attack(
            title="Dragon Tail",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)
