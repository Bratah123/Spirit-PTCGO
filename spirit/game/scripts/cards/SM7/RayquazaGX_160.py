from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    dragon_break,
    stormy_winds,
    tempest_gx,
)
from spirit.game.data_utils import Triggers

card = PokemonCardDef(
    guid="5f1d0bbf-add1-5a1f-b124-636ba61eb319",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaGX.Name",
    display_name="Rayquaza-GX",
    searchable_by=["Rayquaza-GX", "Basic", "GX", "RayquazaGX"],
    subtypes=["Basic", "GX"],
    collector_number=160,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Ability(
            title="Stormy Winds",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard the top 3 cards of your deck. If you do, attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=stormy_winds,
        ),
        Attack(
            title="Dragon Break",
            game_text="This attack does 30 damage times the amount of basic Grass and basic Lightning Energy attached to your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=dragon_break,
        ),
        Attack(
            title="Tempest-GX",
            game_text="Discard your hand and draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=tempest_gx,
        ),
    ],
)