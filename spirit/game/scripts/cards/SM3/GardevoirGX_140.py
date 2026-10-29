from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import fairy_energy_in_hand, infinite_force, secret_spring, twilight_gx

card = PokemonCardDef(
    guid="54dc0953-69e3-5044-a0da-b13be8e80b41",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirGX.Name",
    display_name="Gardevoir-GX",
    searchable_by=["Gardevoir-GX", "Stage 2", "GX", "GardevoirGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=140,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Secret Spring",
            game_text="Once during your turn (before your attack), you may attach a Fairy Energy card from your hand to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=fairy_energy_in_hand,
            effect=secret_spring,
        ),
        Attack(
            title="Infinite Force",
            game_text="This attack does 30 damage times the amount of Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            damage_operator="x",
            effect=infinite_force,
        ),
        Attack(
            title="Twilight-GX",
            game_text="Shuffle 10 cards from your discard pile into your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            effect=twilight_gx,
        ),
    ],
)
