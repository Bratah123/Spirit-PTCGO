from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.sm3 import hydro_shot, tapu_storm_gx


card = PokemonCardDef(
    guid="b60bbaa8-e97e-57e7-89cf-d29cadfbde31",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuFiniGX.Name",
    display_name="Tapu Fini-GX",
    searchable_by=["Tapu Fini-GX", "Basic", "GX", "TapuFiniGX"],
    subtypes=["Basic", "GX"],
    collector_number=171,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=788,
    abilities=[
        Attack(
            title="Aqua Ring",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Hydro Shot",
            game_text="Discard 2 Water Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=hydro_shot,
        ),
        Attack(
            title="Tapu Storm-GX",
            game_text="Shuffle your opponent's Active Pok\u00e9mon and all cards attached to it into their deck. If your opponent has no Benched Pok\u00e9mon, this attack does nothing. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=tapu_storm_gx,
        ),
    ],
)
