from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.ecard import (
    discard_all_typed_energy_flip_damage,
    has_typed_basic_energy,
)


card = PokemonCardDef(
    guid="03ba1522-2525-5ed9-a669-e1f3c8b17345",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesElectabuzz.Name",
    display_name="Lt. Surge's Electabuzz",
    searchable_by=["Lt. Surge's Electabuzz", "Basic", "LtSurgesElectabuzz"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=125,
    abilities=[
        Attack(
            title="Charge",
            game_text="Take up to 2 Lightning Energy cards from your discard pile and attach them to Lt. Surge's Electabuzz.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=attach_from_discard(
                predicate=is_lightning_energy, count=2, minimum=0),
        ),
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy cards attached to Lt. Surge's Electabuzz in order to use this attack. Flip a number of coins equal to the number of Lightning Energy cards you discarded. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="x",
            condition=has_typed_basic_energy(PokemonTypes.LIGHTNING),
            effect=discard_all_typed_energy_flip_damage(
                PokemonTypes.LIGHTNING, 30),
        ),
    ],
)
