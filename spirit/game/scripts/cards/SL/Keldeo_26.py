"""STUB: effect not implemented — do not guess mechanics.
Keldeo (SL #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_water_pokemon

card = PokemonCardDef(
    guid="176a9ad7-f2d2-5efa-a0dd-908db043d265",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic", "Keldeo"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Attack(
            title="Bail Out",
            game_text="Put a Water Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                is_water_pokemon, count=1,
                prompt="Choose a Water Pokémon to put into your hand",
            ),
        ),
        Attack(
            title="Resolute Blade",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 20, base=20),
        ),
    ],
)