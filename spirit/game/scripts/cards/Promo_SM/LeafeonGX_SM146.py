from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import breath_condition, breath_of_the_leaves, grand_bloom_gx

card = PokemonCardDef(
    guid="13e38eb3-5e8c-52b1-afab-c62fd436ddc8",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonGX.Name",
    display_name="Leafeon-GX",
    searchable_by=["Leafeon-GX", "Stage 1", "GX", "LeafeonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=146,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Breath of the Leaves",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, once during your turn (before your attack), you may heal 50 damage from 1 of your Pok\u00e9mon that has any Energy attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=breath_of_the_leaves,
            activation=Activations.ONCE_PER_TURN,
            condition=breath_condition,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Grand Bloom-GX",
            game_text="For each of your Benched Basic Pok\u00e9mon, search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=grand_bloom_gx,
        ),
    ],
)