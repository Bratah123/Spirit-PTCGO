from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.scripts.cards.SM2.TapuKokoGX_47 import aero_trail
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.attacks_common import damage_per, count_energy

card = PokemonCardDef(
    guid="2357cd14-5b6b-5ea8-a414-43c0835a432f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoGX.Name",
    display_name="Tapu Koko-GX",
    searchable_by=["Tapu Koko-GX", "Basic", "GX", "TapuKokoGX"],
    subtypes=["Basic", "GX"],
    collector_number=135,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=785,
    abilities=[
        Ability(
            title="Aero Trail",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may move any number of Lightning Energy from your other Pok\u00e9mon to this Pok\u00e9mon. If you do, switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=aero_trail,
        ),
        Attack(
            title="Sky-High Claws",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Tapu Thunder-GX",
            game_text="This attack does 50 damage times the amount of Energy attached to all of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy('opponent'), 50),
        ),
    ],
)