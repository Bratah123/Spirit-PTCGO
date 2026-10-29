from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.smp import abnormal_overheating, critical_error_gx, troubleshooting, troubleshooting_condition

card = PokemonCardDef(
    guid="5cc94745-1e52-5413-a42b-0fcb2d451bdf",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZGX.Name",
    display_name="Porygon-Z-GX",
    searchable_by=["Porygon-Z-GX", "Stage 2", "GX", "PorygonZGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=216,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=474,
    abilities=[
        Ability(
            title="Troubleshooting",
            game_text="Once during your turn (before your attack), you may discard a Special Energy from this Pok\u00e9mon. If you do, heal 80 damage from it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=troubleshooting,
            activation=Activations.ONCE_PER_TURN,
            condition=troubleshooting_condition,
        ),
        Attack(
            title="Abnormal Overheating",
            game_text="This Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=abnormal_overheating,
        ),
        Attack(
            title="Critical Error-GX",
            game_text="Search your deck for up to 10 cards and discard them. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=critical_error_gx,
        ),
    ],
)