from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import LightsEndPassive, black_ray_gx, prismatic_burst

card = PokemonCardDef(
    guid="88ac58b9-eca6-5a88-b4f0-78c6ac200656",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaGX.Name",
    display_name="Necrozma-GX",
    searchable_by=["Necrozma-GX", "Basic", "GX", "NecrozmaGX"],
    subtypes=["Basic", "GX"],
    collector_number=153,
    set_code="SM3",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Ability(
            title="Light's End",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Colorless Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=LightsEndPassive(),
        ),
        Attack(
            title="Prismatic Burst",
            game_text="Discard all Psychic Energy from this Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=prismatic_burst,
        ),
        Attack(
            title="Black Ray-GX",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=black_ray_gx,
        ),
    ],
)
