from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.pokemon import is_pokemon_vmax

_is_fighting = lambda p: PokemonTypes.FIGHTING.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])
_protects_fighting_team = lambda target, carrier: (
    target.owning_player_id == carrier.owning_player_id and _is_fighting(target)
)
_attacker_is_vmax = lambda attacker: is_pokemon_vmax(attacker.archetype_id)

card = PokemonCardDef(
    guid="f4b957a8-0f26-5aeb-b968-294fdf0bee7e",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    display_name="Zamazenta V",
    searchable_by=["Zamazenta V", "Basic", "V", "ZamazentaV"],
    subtypes=["Basic", "V"],
    collector_number=18,
    set_code="CEL25",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=889,
    abilities=[
        Ability(
            title="Growl of the Shield",
            game_text="All of your Fighting Pok\u00e9mon take 20 less damage from attacks from your opponent's Pok\u00e9mon VMAX (after applying Weakness and Resistance). You can't apply more than 1 Growl of the Shield Ability at a time.",
            passive=takes_less_passive(
                20, protects=_protects_fighting_team,
                attacker_pred=_attacker_is_vmax, stack_key="GrowlOfTheShield",
            ),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)