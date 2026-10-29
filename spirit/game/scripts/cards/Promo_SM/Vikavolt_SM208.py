from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm10 import stealthy_body_passive, electricannon


card = PokemonCardDef(
    guid="061ac64c-5ca1-57cb-a0af-610ad9b2f227",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=208,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=738,
    abilities=[
        Ability(
            title="Stealthy Body",
            game_text="If there is any Stadium card in play, this Pok\u00e9mon has no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=stealthy_body_passive,
        ),
        Attack(
            title="Electricannon",
            game_text="You may discard all Lightning Energy from this Pok\u00e9mon. If you do, this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=120,
            damage_operator="+",
            effect=electricannon,
        ),
    ],
)