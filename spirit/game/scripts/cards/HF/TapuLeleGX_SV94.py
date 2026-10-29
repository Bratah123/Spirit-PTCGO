from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import luminous_sign
from spirit.game.data_utils import Triggers
from spirit.game.scripts.cards.SM2.TapuLeleGX_60 import energy_drive, tapu_cure_gx

card = PokemonCardDef(
    guid="5432bb9b-e396-5bac-a412-f288c463e4bf",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLeleGX.Name",
    display_name="Tapu Lele-GX",
    searchable_by=["Tapu Lele-GX", "Basic", "GX", "TapuLeleGX"],
    subtypes=["Basic", "GX"],
    collector_number=163,
    set_code="HF",
    rarity=Rarities.RareSecret,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=786,
    abilities=[
        Ability(
            title="Wonder Tag",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=luminous_sign,
        ),
        Attack(
            title="Energy Drive",
            game_text="This attack does 20 damage times the amount of Energy attached to both Active Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=energy_drive,
        ),
        Attack(
            title="Tapu Cure-GX",
            game_text="Heal all damage from 2 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=tapu_cure_gx,
        ),
    ],
)