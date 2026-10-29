from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.dm import (
    kyurem_outrage,
)

card = PokemonCardDef(
    guid="9ca7210f-3e74-5a66-99b9-867b36a9f058",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem", "Basic", "Kyurem"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=646,
    abilities=[
        Attack(
            title="Outrage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=kyurem_outrage,
        ),
        Attack(
            title="Frost Spear",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=snipe_attack(20, also_base=True),
        ),
    ],
)