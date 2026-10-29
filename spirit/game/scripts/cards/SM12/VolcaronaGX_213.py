from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import dread_storm_gx
from spirit.game.card_effects.sm12 import backfire, flaming_shot, flaming_shot_condition


card = PokemonCardDef(
    guid="9d16a24b-56eb-5bcc-bd9b-16ae3d26e019",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcaronaGX.Name",
    display_name="Volcarona-GX",
    searchable_by=["Volcarona-GX", "Stage 1", "GX", "VolcaronaGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=213,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Ability(
            title="Flaming Shot",
            game_text="Once during your turn (before your attack), you may discard a Fire Energy card from your hand. If you do, put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=flaming_shot_condition,
            effect=flaming_shot,
        ),
        Attack(
            title="Backfire",
            game_text="Put 2 Fire Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=backfire,
        ),
        Attack(
            title="Massive Heat Wave-GX",
            game_text="Discard an Energy from each of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=dread_storm_gx,
        ),
    ],
)