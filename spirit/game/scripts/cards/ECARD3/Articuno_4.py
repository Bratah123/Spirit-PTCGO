from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    AntiWaterPassive, collect_energy_from_discard, ice_cyclone,
)


card = PokemonCardDef(
    guid="70ae7e58-4d9e-512d-a8a5-14dfe929790f",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Water Immunity",
            game_text="You can't attach Water Energy cards from your hand to Articuno.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=AntiWaterPassive(),
        ),
        Attack(
            title="Freeze Solid",
            game_text="If there are any Water Energy cards in your discard pile, flip a coin. If heads, attach 1 of them to Articuno.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=collect_energy_from_discard(PokemonTypes.WATER),
        ),
        Attack(
            title="Ice Cyclone",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. If tails, this attack does 10 damage to each of your Pok\u00e9mon in play. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ice_cyclone,
        ),
    ],
)
