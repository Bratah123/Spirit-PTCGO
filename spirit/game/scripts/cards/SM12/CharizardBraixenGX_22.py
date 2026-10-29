from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import brilliant_flare, crimson_flame_pillar_gx

card = PokemonCardDef(
    guid="607629bb-04a5-541a-abbd-a8f8d270aebd",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardBraixenGX.Name",
    display_name="Charizard & Braixen-GX",
    searchable_by=["Charizard & Braixen-GX", "Basic", "TAG TEAM", "GX", "CharizardBraixenGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=22,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Brilliant Flare",
            game_text="You may search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=brilliant_flare,
        ),
        Attack(
            title="Crimson Flame Pillar-GX",
            game_text="Attach 5 basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like. If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), your opponent's Active Pok\u00e9mon is now Burned and Confused. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=crimson_flame_pillar_gx,
        ),
    ],
)