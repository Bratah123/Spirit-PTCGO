from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack

from spirit.game.card_effects.sm9 import (
    darkest_tornado_gx,
    scar_charge,
)

card = PokemonCardDef(
    guid="c4305fa5-11fc-5c82-a3c7-85f8575f44e7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IncineroarGX.Name",
    display_name="Incineroar-GX",
    searchable_by=["Incineroar-GX", "Stage 2", "GX", "IncineroarGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=97,
    set_code="SM9",
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Ability(
            title="Scar Charge",
            game_text="Once during your turn (before your attack), you may put 3 damage counters on this Pok\u00e9mon. If you do, search your deck for up to 3 Darkness Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=scar_charge,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Crushing Punch",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Darkest Tornado-GX",
            game_text="This attack does 50 more damage for each damage counter on this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=darkest_tornado_gx,
        ),
    ],
)