from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.ecard import electric_current


card = PokemonCardDef(
    guid="8329d3ba-45c8-5a29-b8e4-fe702a348160",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesElectabuzz.Name",
    display_name="Lt. Surge's Electabuzz",
    searchable_by=["Lt. Surge's Electabuzz", "Basic", "LtSurgesElectabuzz"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=60,
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
            title="Electric Current",
            game_text="Take 1 Lightning Energy card attached to Lt. Surge's Electabuzz and attach it to 1 of your Benched Pok\u00e9mon. If you have no Benched Pok\u00e9mon, discard that Energy card.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            effect=electric_current,
        ),
    ],
)
