from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import LuminousBarrierPassive
from spirit.game.card_effects.pokemon import shred
from spirit.game.card_effects.attacks_common import damage_per, count_bench


card = PokemonCardDef(
    guid="704df74f-27ca-52a2-9afe-6257734db082",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KeldeoGX.Name",
    display_name="Keldeo-GX",
    searchable_by=["Keldeo-GX", "Basic", "GX", "KeldeoGX"],
    subtypes=["Basic", "GX"],
    collector_number=240,
    set_code="SM11",
    rarity=Rarities.RareRainbow,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Ability(
            title="Pure Heart",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=LuminousBarrierPassive(),
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=shred,
        ),
        Attack(
            title="Resolute Blade-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_bench('opponent'), 50),
        ),
    ],
)