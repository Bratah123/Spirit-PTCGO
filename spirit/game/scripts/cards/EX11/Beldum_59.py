"""STUB: effect not implemented — do not guess mechanics.
Beldum δ (EX11 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import conductive_body_beldum_passive, recoil_self
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="1d2b4707-3001-50ee-8e15-9f9cc459d7a8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum δ",
    searchable_by=["Beldum \u03b4", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Ability(
            title="Conductive Body",
            game_text="As long as Beldum is your Active Pok\u00e9mon, you pay Colorless less to retreat Beldum for each Beldum on your Bench.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=conductive_body_beldum_passive('Beldum'),
            effect=None,
        ),
        Attack(
            title="Take Down",
            game_text="Beldum does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_self(10),
        ),
    ],
)